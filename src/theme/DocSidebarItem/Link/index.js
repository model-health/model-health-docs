import React from 'react';
import DocSidebarItemLink from '@theme-original/DocSidebarItem/Link';
import { Rocket, Video, Lightbulb, Settings, BookMarked, PocketKnife } from 'lucide-react';

const iconMap = { Rocket, Video, Lightbulb, Settings, BookMarked, PocketKnife };

function labelWithTitle(jsxNode, titleStr) {
  return new Proxy(jsxNode, {
    get(target, prop, receiver) {
      if (prop === 'toString' || prop === Symbol.toPrimitive) {
        return () => titleStr;
      }
      return Reflect.get(target, prop, receiver);
    },
  });
}

export default function DocSidebarItemLinkWrapper(props) {
  const { item } = props;
  const iconName = item.customProps?.icon;
  const IconComponent = iconName ? iconMap[iconName] : null;

  if (!IconComponent) {
    return <DocSidebarItemLink {...props} />;
  }

  const labelNode = (
    <span style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
      <span className="sidebar-category-icon" style={{ display: 'flex', alignItems: 'center' }}>
        <IconComponent size={15} />
      </span>
      {item.label}
    </span>
  );

  const patchedItem = {
    ...item,
    label: labelWithTitle(labelNode, typeof item.label === 'string' ? item.label : ''),
  };

  return <DocSidebarItemLink {...props} item={patchedItem} />;
}
